def negaternary(i, k):
    if i == 0:
        digits = [0]
    else:
        digits = []
        while i != 0:
            i, remainder = divmod(i, -k)
            if remainder < 0:
                i, remainder = i + 1, remainder + k
            digits.append(remainder)
    return digits


p, k = map(int, input().split())
ans = negaternary(p, k)
# while (p):
# 	ans.append(p % (-k))
# 	p //= (-k)
while(ans[-1] == 0):
	ans = ans[::-1]
print(len(ans))
print(*ans)
