def scan_project():
    name, version_str = input().split()
    return (name, int(version_str))


n = int(input())
projects, depends = [], {}
for i in range(n):
    if i > 0:
        input()
    project = scan_project()
    projects.append(project)
    depends[project] = [scan_project() for j in range(int(input()))]

root_name, root_version = projects[0]
level_depends = [projects[0]]
all_depends = {root_name: root_version}
while level_depends:
    level_depends = list(set([(name, version) for project in level_depends
                              for name, version in depends[project] if name not in all_depends]))
    for name, version in sorted(level_depends):
        all_depends[name] = version
    level_depends = [(name, version) for name, version in level_depends
                     if all_depends[name] == version]

all_depends.pop(root_name)
print(len(all_depends))
for name in sorted(all_depends):
    print(name, all_depends[name])
