(n, x) = map(int, input().split())
watch = 0
now = 1
for i in range(n):
    (s, e) = map(int, input().split())
    watch += (s - now) % x + (e - s) + 1
    now = e + 1
print(watch)
