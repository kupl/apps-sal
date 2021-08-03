n = int(input())
s = input()
print(min(sum([1 if i == '8' else 0 for i in s]), len(s) // 11))
