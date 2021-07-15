def bfs(polycarp, all_projects, existed_projects):
    # print(polycarp)
    # print(all_projects)
    # print(existed_projects)

    queue0 = {polycarp[0]: polycarp[1]}
    queue1 = {}

    while queue0:
        for p in list(queue0.items()):
            existed_projects[p[0]] = p[1]

        for pp in list(queue0.items()):
            for p in all_projects[pp]:
                if p[0] not in existed_projects:
                    if p[0] not in queue1:
                        queue1[p[0]] = p[1]
                    else:
                        queue1[p[0]] = max(queue1[p[0]], p[1])
                else:
                    continue

        queue0, queue1 = queue1, {}


def main():
    n = int(input())
    all_projects = {}
    for _ in range(n):
        name, version = input().split()
        version = int(version)
        if _ == 0:
            polycarp = (name, version)
        nn = int(input())
        all_projects[(name, version)] = []
        for _2 in range(nn):
            name2, version2 = input().split()
            version2 = int(version2)
            all_projects[(name, version)].append((name2, version2))
        if _ != n - 1:
            input()

    existed_projects = {}
    bfs(polycarp, all_projects, existed_projects)

    print(len(existed_projects) - 1)
    for name in sorted(existed_projects.keys()):
        if name != polycarp[0]:
            print(name, existed_projects[name])


def __starting_point():
    main()

__starting_point()
