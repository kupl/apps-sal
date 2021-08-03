n = int(input())
a = list(map(int, input().split()))
done = set()
j = n
for i in range(n):
    done.add(a[i])
    while j in done:
        print(j, end=' ')
        j -= 1
    print()
