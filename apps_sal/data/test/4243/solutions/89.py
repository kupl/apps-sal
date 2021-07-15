X = int(input())

# X円を、500で割り、余りを更に5で割る

happiness = ( X // 500 ) * 1000 + (( X % 500 ) // 5 ) * 5

print(happiness)
