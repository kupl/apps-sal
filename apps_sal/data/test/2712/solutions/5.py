t = int(input())
for you in range(t):
    l = input().split()
    li = [int(i) for i in l]
    print(max(li) + 1)
