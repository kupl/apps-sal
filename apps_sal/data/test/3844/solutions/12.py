n = int(input())
cards = list(map(int, input().split()))
is_odd = {}
for card in cards:
    if card in is_odd:
        is_odd[card] = not is_odd[card]
    else:
        is_odd[card] = False
for card in is_odd:
    if not is_odd[card]:
        print('Conan')
        return
print('Agasa')
