import re


def count_words(s: str, balance: int):
    if balance == 0:
        return 0
    s = list([x for x in s.split('_') if x != ''])
    return len(s)

def get_len(s: str, balance: int):
    if balance == 1:
        return 0
    s = list([x for x in s.split('_') if x != ''])
    if len(s) == 0:
        return 0
    return max(list(map(len, s)))

def main():
    n = int(input())
    text = input()
    balance = 0
    text = re.split(r'[()]', text)
    q = 0
    l = 0
    for i in text:
        q += count_words(i, balance)
        l = max(l, get_len(i, balance))
        if balance == 0:
            balance += 1
        else:
            balance -= 1
    print(l, q)

main()

