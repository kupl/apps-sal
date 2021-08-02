n = int(input())
s = input()
print(sum(s[i:i + 3] == "ABC" for i in range(n - 2)))
