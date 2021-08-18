f = input()
s = input()
day = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
length = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(11):
    if day[(day.index(f) + length[i]) % 7] == s:
        print('YES')
        return
print('NO')
