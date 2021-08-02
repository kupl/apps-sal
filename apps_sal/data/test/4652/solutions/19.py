'''q=int(input())
for I in range(q):
    n=int(input())
    a=[int(i) for i in input().split()]
    ind = a.find(1)
    ini = [(i+1) for i in range(n)]
    arr1 = a[ind:]
    arr2 = a[:ind]
    if(sorted(arr1)==a['''


def main():
    t = int(input())
    for q in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]

        idx = a.index(1)

        b = a[idx:] + a[: idx]
        c = a[: idx + 1][::-1] + a[idx + 1:][::-1]

        a.sort()

        if b == a or c == a:
            print("YES")
        else:
            print("NO")


main()
