s1, s2, s3 = list(map(str, input().split()))

def three_letter_acronym() -> str:
    return (s1[0] + s2[0] + s3[0])
print(three_letter_acronym().upper())
