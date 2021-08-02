k = int(input())

div = k // 50
mod = k % 50
A = [100 + div - mod] * mod + [49 + div - mod] * (50 - mod)
print((50))
print((*A))
