from collections import Counter

def check():
    pwd = input()
    hsh = input()
    pctr = Counter(pwd)
    ctr = Counter(hsh[:len(pwd)])
    if pctr == ctr:
        return 'YES'
    for i in range(len(hsh)-len(pwd)):
        ctr[hsh[i]] -= 1
        if ctr[hsh[i]] == 0:
            del ctr[hsh[i]]
        ctr[hsh[i+len(pwd)]] += 1
        if pctr == ctr:
            return 'YES'
    return 'NO'

for tcase in range(int(input())):
    print(check())
    

