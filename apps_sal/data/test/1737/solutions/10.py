# python3

def read_project_name():
    name, version = input().split()
    return (name, int(version))


def read_project():
    project = read_project_name()
    deps = list()

    dependencies = int(input())
    while(dependencies):
        dependencies -= 1
        deps.append(read_project_name())

    return (project, tuple(deps))


def main():
    dependencies = dict()
    n = int(input()) - 1

    main_project, deps = read_project()
    dependencies[main_project] = deps
    queue = (main_project, )

    while n:
        n -= 1
        input()
        project, deps = read_project()
        dependencies[project] = deps

    selected = dict()
    while queue:
        new_selected = dict()
        for (name, version) in queue:
            if name not in selected:
                old = new_selected.get(name, -1)
                new_selected[name] = max(old, version)

        queue = list()
        for project in new_selected.items():
            queue.extend(dependencies[project])

        selected.update(new_selected)

    del selected[main_project[0]]
    print(len(selected))
    for (project, ver) in sorted(selected.items()):
        print(project, ver)


main()
