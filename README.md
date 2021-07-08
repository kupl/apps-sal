# APPS dataset refined by SAL
APPS is a python coding competition dataset.
The original contents can be found in [here](https://github.com/hendrycks/apps).

## Refined
We (SAL, Software Analysis Laboratory) refined the original dataset.
All the modified data have `README.txt` in directory.
The major modifications are as follows:
* Fill missing `input_output.json`.
* Use ellipsis (`...`) as placeholder in `starter_code.py`.

## Installation
You can install `apps-sal` using `pip3`.

### Requirement
`apps-sal` requires python 3.7 or higher.

### Install Commands
If you set ssh authentication with GitHub, you can install `apps-sal` by simply typing a following command:
```bash
$ [sudo] pip3 install git+ssh://git@github.com/kupl/apps-sal.git
```
If you do not use ssh authentication, you can install `apps-sal` with following commands:
```bash
$ git clone https://github.com/kupl/apps-sal.git
$ cd apps-sal
apps-sal $ [sudo] pip3 install .
```

### Examples
You can load APPS train set with the following codes:
```python
import apps_sal

train = apps_sal.load_train_dataset()
```
