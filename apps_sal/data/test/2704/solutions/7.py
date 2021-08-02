n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
start = a[0]
end = a[n - 1]
for i in range(q):
    num = int(input())
    if(start <= num <= end):
        print("Yes")
    else:
        print("No")
