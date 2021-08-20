N = int(input())
card_list = list(map(int, input().split()))
card_list.sort(reverse=True)
card_list_Alice = card_list[::2]
Alice_score = sum(card_list_Alice)
Bob_score = sum(card_list) - Alice_score
print(Alice_score - Bob_score)
