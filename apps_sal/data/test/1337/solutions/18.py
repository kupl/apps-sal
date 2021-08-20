def parse_int():
    return list(map(int, input().split()))


scientists = int(input())
sc_langs = parse_int()
films = int(input())
film_voice = parse_int()
film_sub = parse_int()
lang_decoder = dict()
lang_decoder.setdefault(0)
for _ in sc_langs:
    if _ in list(lang_decoder.keys()):
        lang_decoder[_] += 1
    else:
        lang_decoder[_] = 1
(film_good, film_ok) = ([0] * films, [0] * films)
for _ in range(films):
    try:
        film_good[_] += lang_decoder[film_voice[_]] or 0
    except KeyError:
        pass
    try:
        film_ok[_] += lang_decoder[film_sub[_]] or 0
    except KeyError:
        pass
best = 0
for _ in range(films):
    if film_good[_] > film_good[best]:
        best = _
    if film_good[_] == film_good[best] and film_ok[_] > film_ok[best]:
        best = _
print(best + 1)
