# 3つリストを作って、各頭文字をくっつけた略語をアッパー

s1, s2, s3 = list(map(list, input().split()))
# print(s1)
# print(s2)
# print(s3)

abbreviation = s1[0] + s2[0] + s3[0]
# print(abbreviation)

print((abbreviation.upper()))

