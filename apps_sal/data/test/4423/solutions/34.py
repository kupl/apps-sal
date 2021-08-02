N = int(input())
book = []
for i in range(N):
    city, sco = input().split()
    sco = int(sco)
    book.append({'city': city, 'score': sco, 'number': i + 1})

book.sort(key=lambda x: (x['city'], -x['score']))

for j in range(N):
    print((book[j]['number']))
