franxx = int(input())
life = input()
life = life.split()
darling = {}
for i in range(0, franxx):
    tmp = 0
    for j in range(i, franxx):
        tmp += int(life[j])
        darling[tmp] = (franxx, 0)
oh_pay = 'I love my darling'
for i in range(franxx, 0, -1):
    tmp = 0
    for j in range(i - 1, franxx):
        tmp += int(life[j])
        if darling[tmp][0] > j:
            darling[tmp] = (i - 1, 1 + darling[tmp][1])
            if oh_pay == 'I love my darling' or darling[tmp][1] > darling[oh_pay][1]:
                oh_pay = tmp
print(darling[oh_pay][1])
darling[oh_pay] = (franxx, 0)
for i in range(franxx, 0, -1):
    tmp = 0
    for j in range(i - 1, franxx):
        tmp += int(life[j])
        if tmp != oh_pay:
            continue
        if darling[oh_pay][0] > j:
            print(i, j + 1)
            darling[oh_pay] = (i - 1, 1 + darling[oh_pay][1])
