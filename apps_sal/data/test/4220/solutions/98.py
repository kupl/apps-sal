n = int(input())
li = list(input())
if len(li) > n:
    for i in range(n):
        print(li[i], end="")
    print("...")
else:
    for i in range(len(li)):
        print(li[i], end="")
