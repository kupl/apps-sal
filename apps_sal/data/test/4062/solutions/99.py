(a, b, c, d) = map(int, input().split())
ans_list = [a * c, a * d, b * c, b * d]
ans_list.sort()
ans = ans_list.pop()
print(ans)
