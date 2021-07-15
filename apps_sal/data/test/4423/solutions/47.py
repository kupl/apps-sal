
url = "https://atcoder.jp//contests/abc128/tasks/abc128_b"

def main():
    n = int(input())
    town = {}
    rate = []
    for i in range(n):
        t = list(input().split())
        town.setdefault(t[0], {})
        town[t[0]][i+1] = int(t[1])
    town = sorted(list(town.items()), key=lambda x:x[0])
    for k in town:
        sort_town = sorted(list(k[1].items()), key=lambda x:x[1], reverse=True)
        for v in sort_town:
            print((v[0]))


def __starting_point():
    main()

__starting_point()
