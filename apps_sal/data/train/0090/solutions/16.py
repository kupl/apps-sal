def main():
    n = int(input())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    new_lst = []
    for i in range(n):
        if not l[i]:
            new_lst.append(a[i])
    new_lst = sorted(new_lst, reverse=True)
    k = 0
    for i in range(n):
        if not l[i]:
            a[i] = new_lst[k]
            k += 1
    sm = 0
    for i in a:
        print(i, end=" ")
    print()

def __starting_point():
    t = int(input())
    for i in range(t):
        main()

__starting_point()
