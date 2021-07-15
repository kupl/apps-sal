def isSame(n):
    if n[0] == n[1] and n[1] == n[2]:
        return True
    else:
        return False

n_s = input()
n_i = int(n_s)

while True:
    if isSame(n_s):
        print(n_s)
        break
    else:
        n_i += 1
        n_s = str(n_i)

