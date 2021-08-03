a = int(input())
b = sum(list(map(int, list(str(a)))))
ans = a % b
print("Yes" if ans == 0 else"No")
