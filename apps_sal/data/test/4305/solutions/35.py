h, a = map(int, input().split())
print(h // a + 1 if h % a != 0 else h // a)
