from collections import defaultdict

def __starting_point():

    n, k = list(map(int, input().split()))

    list_ = list(map(int, input().split()))

    if k > n:
        print("NO")
        return

    result = []
    colors = set(range(1, k+1))

    total_used = set()
    used = defaultdict(set)

    for i in list_:
        free_colors = colors - used[i]
        priority_colors = free_colors - total_used
        if not free_colors:
            print("NO")
            return
        else:
            if priority_colors:
                color = priority_colors.pop()
            else:
                color = free_colors.pop()

            total_used.add(color)
            used[i].add(color)
            result.append(color)

    print("YES")
    for el in result:
        print(el, end=' ')

__starting_point()
