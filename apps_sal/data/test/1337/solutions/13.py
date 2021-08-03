def which_movie(n, m, langs_ix, audio_ix, subs_ix):
    langs = {}
    for l in langs_ix:
        if l in langs:
            langs[l] += 1
        else:
            langs[l] = 1
    scores = []
    for i in range(m):
        vp = langs[audio_ix[i]] if audio_ix[i] in langs else 0
        asp = langs[subs_ix[i]] if subs_ix[i] in langs else 0
        scores.append((i + 1, vp, asp))

    scores = sorted(scores, key=lambda x: (x[1], x[2], -x[0]))
    return scores[-1][0]


def main():
    n = int(input().strip())
    lang_ix = [int(i) for i in input().strip().split()]
    m = int(input().strip())
    audiolang_ix = [int(i) for i in input().strip().split()]
    subtitle_ix = [int(i) for i in input().strip().split()]
    ans = which_movie(n, m, lang_ix, audiolang_ix, subtitle_ix)
    print(ans)


def __starting_point():
    main()


__starting_point()
