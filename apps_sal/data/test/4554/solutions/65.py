w, a, b = map(int, input().split())
print(0) if a+w >= b and b+w >= a else print(b-a-w) if a+w < b else print(a-b-w)
