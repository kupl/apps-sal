import sys


def convert_string(string_list, len_string_list):
    change_dict = {}
    change_dict['9'] = '6'
    change_dict['5'] = '2'
    for i in range(len_string_list):
        if string_list[i] in change_dict:
            string_list[i] = change_dict[string_list[i]]


def form_frequency_dict(given_list):
    freq_dict = {}
    for i in given_list:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1
    return freq_dict


def find_max_repititions(required_string_freq_dict, given_string_freq_dict):
    max_repititions = 201
    for (key, value) in required_string_freq_dict.items():
        if key in given_string_freq_dict:
            max_repititions_now_possible = given_string_freq_dict[key] // required_string_freq_dict[key]
            if max_repititions_now_possible < max_repititions:
                max_repititions = max_repititions_now_possible
    if max_repititions == 201:
        max_repititions = 0
    return max_repititions


inputlist = sys.stdin.readlines()
required_string = list(inputlist[0].strip())
given_string = list(inputlist[1].strip())
len_required_string = len(required_string)
len_given_string = len(given_string)
convert_string(required_string, len_required_string)
convert_string(given_string, len_given_string)
required_string_freq_dict = form_frequency_dict(required_string)
given_string_freq_dict = form_frequency_dict(given_string)
max_repititions = find_max_repititions(required_string_freq_dict, given_string_freq_dict)
print(max_repititions)
