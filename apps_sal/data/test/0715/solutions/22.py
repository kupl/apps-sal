answers = ['A', 'B', 'C', 'D']
variants = []
for i in range(0, 4):
    variants.append((len(input()) - 2, answers[i]))
asc = sorted(variants, key=lambda variant: variant[0])
des = sorted(variants, key=lambda variant: variant[0], reverse = True)

good_variants = []
if (2 * asc[0][0] <= asc[1][0]):
    good_variants.append(asc[0])
if (2 * des[1][0] <= des[0][0]):
    good_variants.append(des[0])
print(good_variants[0][1] if len(good_variants) == 1 else 'C')
