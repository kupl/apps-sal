def calc_T_shirt_winner_places(s):
    """
    i := (s div 50) mod 475
repeat 25 times:
    i := (i * 96 + 42) mod 475
    print (26 + i)
    """
    i = s // 50 % 475
    i_indices = set()
    for j in range(25):
        i = (i * 96 + 42) % 475
        i_indices.add(26 + i)
    return i_indices


def reachable_by_unsuccessful_hacks(wanted_place, orig_score, min_place):
    score = orig_score
    while score >= min_place:
        if wanted_place in calc_T_shirt_winner_places(score):
            return True
        score -= 50
    if wanted_place in calc_T_shirt_winner_places(score) and score >= min_place:
        return True
    return False


def calc_number_of_successful_hacks_needed(wanted_place, orig_score):
    hacks = 0
    (score_by_50, score_by_100) = (orig_score + 50, orig_score + 100)
    while True:
        hacks += 1
        if score_by_50 >= min_place and wanted_place in calc_T_shirt_winner_places(score_by_50) or (score_by_100 >= min_place and wanted_place in calc_T_shirt_winner_places(score_by_100)):
            return hacks
        score_by_50 += 100
        score_by_100 += 100


(codecraft_place, curr_score, min_place) = [int(p) for p in input().split()]
if reachable_by_unsuccessful_hacks(codecraft_place, curr_score, min_place):
    print(0)
else:
    print(calc_number_of_successful_hacks_needed(codecraft_place, curr_score))
