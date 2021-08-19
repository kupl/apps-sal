n = int(input())
l = list(map(int, input().split()))
mod_check = 0
mod_check_ = 0
for i in l:
    if i % 2 == 0:
        mod_check += 1
        if i % 3 == 0 or i % 5 == 0:
            mod_check_ += 1
        else:
            pass
    else:
        pass
print('APPROVED') if mod_check == mod_check_ else print('DENIED')
