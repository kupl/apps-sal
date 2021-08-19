# A - Three-letter acronym

# s1 s2 s3
s1, s2, s3 = list(map(str, input().split(maxsplit=3)))

answer = s1[0].upper() + s2[0].upper() + s3[0].upper()

print(answer)
