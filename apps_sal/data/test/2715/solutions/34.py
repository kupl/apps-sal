k = int(input())

ans = [49 + k//50 - k%50 + 51] * (k%50) + [49 + k//50 - k%50] * (50-k%50)

print(50)
print(*ans)
