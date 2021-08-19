(a, b, c, d) = map(int, input().split())
product_list = [a * c, a * d, b * c, b * d]
ans = max(product_list)
print(ans)
