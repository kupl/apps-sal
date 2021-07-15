import itertools

def b175(n, llist):

    ans = 0

    itelist = list(itertools.combinations(range(len(llist)), 3))

    for a, b, c in itelist:
        if (llist[a]+llist[b] > llist[c]
                and llist[b]+llist[c] > llist[a]
                and llist[c]+llist[a] > llist[b]
                and llist[a] != llist[b] and llist[b] != llist[c] and llist[c] != llist[a]):
           ans += 1

    return ans

def main():
    n = int(input())
    llist = list(map(int, input().split()))
    print(b175(n, llist))

def __starting_point():
    main()
__starting_point()
