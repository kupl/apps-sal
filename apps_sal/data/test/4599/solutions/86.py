N = input()
card = list(map(int, input().split()))
A = []
B = []
t = 'A'
while card:
    if t == 'A':
        A.append(max(card))
        card.remove(max(card))
        t = 'B'
    else:
        B.append(max(card))
        card.remove(max(card))
        t = 'A'
print(sum(A) - sum(B))
