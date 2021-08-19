def readline():
    return input()


def read_project():
    project = readline().split(' ')
    project[1] = int(project[1])
    dep_num = int(readline())
    deps = {}
    for _ in range(0, dep_num):
        (proj, version) = readline().split(' ')
        version = int(version)
        if proj in deps:
            deps[proj] = max(deps[proj], version)
        else:
            deps[proj] = version
    return (tuple(project), deps)


def make_like_buck():
    projects_num = int(readline())
    projects = {}
    polikarp_proj = None
    for ind in range(0, projects_num):
        (proj, deps) = read_project()
        if ind == 0:
            polikarp_proj = proj
        projects[proj] = deps
        if ind != projects_num - 1:
            readline()
    RESULT_DEPS = {polikarp_proj[0]: polikarp_proj[1]}
    curr_proj = [polikarp_proj]
    while len(curr_proj) > 0:
        curr_deps = {}
        for proj in curr_proj:
            new_deps = projects[proj]
            for proj in new_deps:
                if proj in RESULT_DEPS:
                    continue
                if proj in curr_deps:
                    curr_deps[proj] = max(curr_deps[proj], new_deps[proj])
                else:
                    curr_deps[proj] = new_deps[proj]
        RESULT_DEPS = {**RESULT_DEPS, **curr_deps}
        curr_proj = list(curr_deps.items())
    RESULT_DEPS.pop(polikarp_proj[0])
    print(len(RESULT_DEPS))
    items = ['%s %s' % x for x in sorted(list(RESULT_DEPS.items()))]
    print('\n'.join(items))


make_like_buck()
