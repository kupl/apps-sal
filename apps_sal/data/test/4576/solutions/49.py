a_coins = int(input())
b_coins = int(input())
c_coins = int(input())
x_num = int(input())

def money_match(a, b, c):
    money = 500 * a + 100 * b + 50 * c
    if money == x_num:
        return 1
    else:
        return 0
        
cnt = 0
for a in range(a_coins+1):
    for b in range(b_coins+1):
        for c in range(c_coins+1):
            if money_match(a, b, c) == 1:
                cnt += 1
                
print(cnt)
