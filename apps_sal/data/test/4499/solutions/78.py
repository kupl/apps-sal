# 3つの単語を入力で受け取る
s1, s2, s3 = input().split()
# それぞれの頭文字を集めて大文字
short = str.upper(s1[0] + s2[0] + s3[0])
print(short)
