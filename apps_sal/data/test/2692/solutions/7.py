# cook your dish here
for i in range(int(input())):
    a, b = list(map(int, input().split()))
    print(a - int(((a - 1) / b)))
