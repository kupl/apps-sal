s = input()
prev = s[0]
for i in range(1, 4):
    if s[i] == prev:
        print('Bad')
        return
    prev = s[i]
print('Good')
