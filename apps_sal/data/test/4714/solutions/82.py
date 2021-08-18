
def judege_palindromic(val_str):
    length = len(val_str)
    match = True
    for i in range(length // 2):
        if val_str[i] != val_str[length - i - 1]:
            match = False
            break

    return match


A, B = map(int, input().split())

cnt = 0
for i in range(A, B + 1, 1):
    if judege_palindromic(str(i)):
        cnt += 1

print(cnt)
