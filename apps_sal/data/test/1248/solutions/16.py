#n = int(input())

a, b, c = [int(i) for i in input().split(" ")]
ans = []
ans.append(2 * (a + b))
ans.append((min(a, b) + c) * 2)
ans.append(a + b + c)
print(min(ans))
