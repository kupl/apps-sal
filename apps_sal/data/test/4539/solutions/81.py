n = int(input())
if n % sum(map(int, list(str(n)))) == 0:
    print("Yes")
else:
    print("No")
