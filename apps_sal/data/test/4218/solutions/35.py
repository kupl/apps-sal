a = int(input())
b = 0
for i in range(1, a + 1):
    if i % 2 != 0:
        b += 1
sub = b / a
print(sub)
