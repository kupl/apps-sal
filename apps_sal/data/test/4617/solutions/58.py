# A - Rotation
# https://atcoder.jp/contests/abc077/tasks/abc077_a

a = input()
b = input()

result = 'YES'
i = 0
j = -1
while i < len(a):
    if a[i] != b[j]:
        result = 'NO'
        break
    i += 1
    j -= 1

print(result)
