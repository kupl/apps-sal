from sys import stdin, stdout # only need for big input

def increment_dict(a_dict, element):
    if element in a_dict:
        a_dict[element] = a_dict[element] + 1
    else:
        a_dict[element] = 1

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    mp = dict()
    best_count = 0
    for num in a:
        increment_dict(mp, num)
        increment_dict(mp, num - 1)
        increment_dict(mp, num + 1)
        best_count = max(best_count, mp[num], mp[num-1], mp[num+1])
    print(best_count)

def main():
    solve()


def __starting_point():
    main()
__starting_point()
