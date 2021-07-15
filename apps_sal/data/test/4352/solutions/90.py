#   AtCoder abc054 a
#   ストレッチ課題

#   入力
alice, bob = list(map(int, input().split()))

#   判定
if alice == bob:
    print("Draw")
elif (alice == 1) or ((bob != 1) and (alice > bob)):
    print("Alice")
else:
    print("Bob")

